function submitForm() {
    const numberInput = document.getElementById('numberInput').value;

    if (numberInput) {
        fetch('//API輸入處', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ number: numberInput })
        })
        .then(response => response.json())
        .then(data => {
            displayChart(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        alert('請輸入一個編號！');
    }
}

function displayChart(blob) {
    const chartContainer = document.getElementById('chartContainer');
    chartContainer.innerHTML = '<h3>返回的圖表：</h3>';
    
    const chartImage = document.createElement('img');
    chartImage.src = URL.createObjectURL(blob);
    chartImage.alt = '後端返回的圖表';
    chartContainer.appendChild(chartImage);
}