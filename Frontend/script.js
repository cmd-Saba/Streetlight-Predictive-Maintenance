function sendData() {
  const fileInput = document.getElementById("csvFile");
  const file = fileInput.files[0];
  if (!file) {
    alert("Please upload a CSV file first.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      const resultsDiv = document.getElementById("results");
      resultsDiv.innerHTML = "<h3>Prediction Results:</h3>";
      data.forEach((row, idx) => {
        resultsDiv.innerHTML += `<p><strong>Row ${idx + 1}</strong> - ${row['Failure Prediction']} | ${row['Predicted Time to Failure (hrs)']} hrs</p>`;
      });
    })
    .catch(err => {
      alert("Error while predicting: " + err);
    });
}
