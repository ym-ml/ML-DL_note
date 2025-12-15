// 诊断脚本：查看网格线实际情况
console.log("=== Excalidraw 网格诊断 ===");

// 1. 查看所有SVG和路径
const svgs = document.querySelectorAll('.excalidraw .canvas svg');
console.log(`找到 ${svgs.length} 个SVG元素`);

svgs.forEach((svg, i) => {
  const paths = svg.querySelectorAll('path');
  const rects = svg.querySelectorAll('rect');
  console.log(`SVG ${i}: ${paths.length} paths, ${rects.length} rects`);
  
  // 查看前几个路径的属性
  paths.forEach((path, j) => {
    if (j < 5) { // 只看前5个
      console.log(`  路径 ${j}:`, {
        d: path.getAttribute('d')?.substring(0, 50) + '...',
        stroke: path.getAttribute('stroke'),
        strokeWidth: path.getAttribute('stroke-width'),
        class: path.className,
        transform: path.getAttribute('transform')
      });
    }
  });
});

// 2. 查看Excalidraw API状态
const api = ea.getExcalidrawAPI();
if (api) {
  const state = api.getAppState();
  console.log("API网格状态:", {
    gridModeEnabled: state.gridModeEnabled,
    gridColor: state.gridColor,
    gridMajorColor: state.gridMajorColor,
    gridSize: state.gridSize
  });
}

console.log("=== 诊断结束 =\==");