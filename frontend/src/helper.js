// general function to communicate with backend and complete requests
function fetchData(method, path, body, token) {
  return new Promise((resolve, reject) => {
    let header = [];

    if (token == null) {
      header = { "Content-type": "application/json" };
    } else {
      header = { "Content-type": "application/json", token: token };
    }

    const init = {
      method: method,
      headers: header,
      body: method === "GET" ? undefined : JSON.stringify(body),
    };

    fetch(`http://localhost:5001/${path}`, init)
      .then((response) => {
        return response.json();
      })
      .then((body) => {
        if ("code" in body) {
          if (body.code === 404) {
            resolve(body);
          } else if (body.code !== 200) {
            alert(body.message);
          } else {
            resolve(body);
          }
        } else {
          resolve(body);
        }
      });
  });
}

export default fetchData;

// code adapted from COMP6080
export function fileToDataUrl(file) {
  // converts image file to base 64 encoding
  const validFileTypes = ["image/jpeg", "image/png", "image/jpg"];
  const valid = validFileTypes.find((type) => type === file.type);
  if (!valid) {
    alert("provided file is not a png, jpg or jpeg image.");
    throw Error("provided file is not a png, jpg or jpeg image.");
  }

  const reader = new FileReader();
  const dataUrlPromise = new Promise((resolve, reject) => {
    reader.onerror = reject;
    reader.onload = () => resolve(reader.result);
  });
  reader.readAsDataURL(file);
  return dataUrlPromise;
}
