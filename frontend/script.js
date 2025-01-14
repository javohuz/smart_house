async function toggleLight() {
  const response = await fetch('/toggle-device/1/');
  const data = await response.json();
  alert(`Light is now: ${data.status ? "ON" : "OFF"}`);
}
