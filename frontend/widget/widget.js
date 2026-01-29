
(function(){
  const root = document.createElement('div');
  root.innerHTML = `
    <div style="border:1px solid #ddd;padding:12px;border-radius:8px">
      <h3>Virtual Try-On</h3>
      <input type="file" id="userImg" /><br/>
      <input type="file" id="garmentImg" /><br/>
      <button id="run">Try It On</button>
      <pre id="out"></pre>
    </div>`;
  document.currentScript.parentNode.insertBefore(root, document.currentScript);

  document.getElementById('run').onclick = async () => {
    const fd = new FormData();
    fd.append('user_image', document.getElementById('userImg').files[0]);
    fd.append('garment_image', document.getElementById('garmentImg').files[0]);
    const res = await fetch('/tryon/image', {method:'POST', body: fd});
    document.getElementById('out').innerText = await res.text();
  };
})();
