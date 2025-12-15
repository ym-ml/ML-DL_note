// 最安全方案：只使用API + 极简CSS
const api = ea.getExcalidrawAPI();
if (!api) {
  new Notice("Excalidraw API 加载失败", 3000);
  return;
}

// 1. 只使用API（最安全）
try {
  const state = api.getAppState();
  
  // 先关闭网格再打开，触发重新渲染
  api.updateScene({
    appState: {
      ...state,
      gridModeEnabled: false
    },
    commitToHistory: false
  });
  
  // 延迟后重新打开并设置颜色
  setTimeout(() => {
    api.updateScene({
      appState: {
        ...api.getAppState(),
        gridSize: 20,
        gridStep: 3,
        gridModeEnabled: true,
        gridMode: "advanced",
        gridColor: "#f0f9ff",
        gridMajorColor: "#87ceeb",
        gridOpacity: 0.8
      },
      commitToHistory: false
    });
    
    new Notice("网格已通过API安全设置", 3000);
  }, 100);
  
} catch (error) {
  console.error("API设置失败:", error);
  
  // 2. 如果API失败，使用最简CSS（只针对明确是网格线的元素）
  const minimalStyle = document.createElement('style');
  minimalStyle.textContent = `
    /* 仅修改可能的网格线，不影响其他 */
    .excalidraw .canvas svg[aria-label*="grid"] path,
    .excalidraw .canvas svg[data-type*="grid"] path {
      stroke: #f0f9ff !important;
    }
    
    /* 粗网格线 */
    .excalidraw .canvas svg[aria-label*="grid"] path:nth-child(3n),
    .excalidraw .canvas svg[data-type*="grid"] path:nth-child(3n) {
      stroke: #87ceeb !important;
    }
  `;
  document.head.appendChild(minimalStyle);
  
  new Notice("已使用最小化CSS设置网格", 3000);
}

// 3. 10秒后自动清理CSS（如果使用了）
setTimeout(() => {
  const style = document.querySelector('style[data-grid-temp]');
  if (style) {
    style.remove();
    console.log("临时CSS已清理");
  }
}, 10000);