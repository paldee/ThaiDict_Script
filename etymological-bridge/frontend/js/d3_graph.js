// ==========================================================================
// D3.js Force-Directed Genealogical Tree Visualizer
// ==========================================================================

let simulation = null;
let svg = null;
let gContainer = null;
let zoomBehavior = null;
let isPhysicsActive = true;

const COLOR_MAP = {
  pie_root: "#f59e0b",          // Golden Amber
  branch: "#8b5cf6",            // Cosmic Violet
  intermediate_lang: "#38bdf8", // Sky Blue
  thai_leaf: "#10b981",         // Emerald Green
  english_leaf: "#06b6d4"       // Cyan Neon
};

function initD3Graph() {
  svg = d3.select("#d3GraphSvg");
  svg.selectAll("*").remove(); // clean previous if any

  const width = svg.node().getBoundingClientRect().width || 900;
  const height = 560;

  // Setup Zoom & Pan
  gContainer = svg.append("g").attr("class", "zoomable-container");

  zoomBehavior = d3.zoom()
    .scaleExtent([0.4, 2.5])
    .on("zoom", (event) => {
      gContainer.attr("transform", event.transform);
    });

  svg.call(zoomBehavior);

  // Setup buttons
  document.getElementById("graphResetZoomBtn").onclick = () => {
    svg.transition().duration(500).call(zoomBehavior.transform, d3.zoomIdentity);
  };

  document.getElementById("graphTogglePhysicsBtn").onclick = () => {
    if (simulation) {
      if (isPhysicsActive) {
        simulation.stop();
        document.getElementById("graphTogglePhysicsBtn").innerText = "▶ เริ่มฟิสิกส์";
      } else {
        simulation.restart();
        document.getElementById("graphTogglePhysicsBtn").innerText = "⏸ หยุดฟิสิกส์";
      }
      isPhysicsActive = !isPhysicsActive;
    }
  };
}

function renderD3Graph(graphData) {
  if (!svg) initD3Graph();

  gContainer.selectAll("*").remove();

  const width = svg.node().getBoundingClientRect().width || 900;
  const height = 560;

  document.getElementById("graphTitle").innerText = `ผังเครือญาติภาษาศาสตร์ของคำว่า "${graphData.thai_word}" (ราก ${graphData.pie_root})`;

  const nodes = graphData.nodes.map(d => Object.assign({}, d));
  const links = graphData.links.map(d => Object.assign({}, d));

  // Initialize Force Simulation
  simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).id(d => d.id).distance(d => {
      if (d.source.type === "pie_root" || d.target.type === "pie_root") return 110;
      return 85;
    }))
    .force("charge", d3.forceManyBody().strength(-350))
    .force("center", d3.forceCenter(width / 2, height / 2))
    .force("collide", d3.forceCollide().radius(d => (d.radius || 20) + 12));

  // Render Links
  const link = gContainer.append("g")
    .attr("class", "links")
    .selectAll("line")
    .data(links)
    .enter().append("line")
    .attr("stroke", "rgba(255, 255, 255, 0.18)")
    .attr("stroke-width", 1.8)
    .attr("stroke-dasharray", d => d.source.type === "pie_root" ? "3 3" : "none");

  // Render Link Labels
  const linkText = gContainer.append("g")
    .attr("class", "link-labels")
    .selectAll("text")
    .data(links)
    .enter().append("text")
    .text(d => d.label || "")
    .attr("font-size", "9px")
    .attr("fill", "rgba(255, 255, 255, 0.4)")
    .attr("font-family", "Prompt, sans-serif")
    .attr("text-anchor", "middle");

  // Render Nodes Container
  const node = gContainer.append("g")
    .attr("class", "nodes")
    .selectAll("g")
    .data(nodes)
    .enter().append("g")
    .call(d3.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended));

  // Node Outer Glow Circles
  node.append("circle")
    .attr("r", d => (d.radius || 20) + 4)
    .attr("fill", d => COLOR_MAP[d.type] || "#64748b")
    .attr("opacity", 0.25)
    .attr("filter", "blur(4px)");

  // Node Core Circle
  node.append("circle")
    .attr("r", d => d.radius || 20)
    .attr("fill", d => COLOR_MAP[d.type] || "#334155")
    .attr("stroke", "#ffffff")
    .attr("stroke-width", 1.5)
    .style("cursor", "pointer")
    .on("mouseover", handleMouseOver)
    .on("mouseout", handleMouseOut);

  // Node Text Labels
  node.append("text")
    .text(d => d.name)
    .attr("font-family", "Outfit, Prompt, sans-serif")
    .attr("font-size", d => d.type === "pie_root" ? "12px" : "11px")
    .attr("font-weight", d => d.type === "pie_root" ? "700" : "500")
    .attr("fill", "#ffffff")
    .attr("text-anchor", "middle")
    .attr("dy", d => (d.radius || 20) + 14);

  // Simulation Tick
  simulation.on("tick", () => {
    link
      .attr("x1", d => d.source.x)
      .attr("y1", d => d.source.y)
      .attr("x2", d => d.target.x)
      .attr("y2", d => d.target.y);

    linkText
      .attr("x", d => (d.source.x + d.target.x) / 2)
      .attr("y", d => (d.source.y + d.target.y) / 2 - 4);

    node
      .attr("transform", d => `translate(${d.x},${d.y})`);
  });

  function dragstarted(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }

  function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
  }

  function dragended(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }

  // Tooltip Mechanics
  const tooltip = document.getElementById("graphTooltip");
  const tooltipTitle = document.getElementById("tooltipTitle");
  const tooltipEra = document.getElementById("tooltipEra");
  const tooltipBody = document.getElementById("tooltipBody");

  function handleMouseOver(event, d) {
    tooltipTitle.innerText = d.name;
    tooltipEra.innerText = d.era || "Historical Stage";

    let bodyText = "";
    if (d.type === "pie_root") {
      bodyText = `รากภาษาบรรพบุรุษอินโด-ยูโรเปียนดั้งเดิม\nความหมายเดิม: "${d.meaning}"`;
    } else if (d.type === "thai_leaf") {
      bodyText = `คำในภาษาไทย\nชนิดคำ: ${d.pos || "น."}\nนิยาม: ${d.definition || "-"}`;
    } else if (d.type === "english_leaf") {
      bodyText = `ภาษา: ${d.origin || "English"}\nวิวัฒนาการ: ${d.derivation || "-"}\nหมายเหตุ: ${d.usage_note || "-"}`;
    } else {
      bodyText = `สายการแยกแขนงตระกูลภาษา`;
    }

    tooltipBody.innerText = bodyText;
    tooltip.style.display = "block";
    tooltip.style.left = `${event.offsetX + 15}px`;
    tooltip.style.top = `${event.offsetY - 20}px`;
  }

  function handleMouseOut() {
    tooltip.style.display = "none";
  }
}
