let btn = document.getElementById("buttonFile");
let textFile = document.getElementById("textFile");
console.log($.fn.jquery);   
$.ajaxSetup({
    async: false
});
btn.addEventListener('click', () => {
    var formData = new FormData();
    formData.append('file', $('input[type=file]')[0].files[0]);
    $.ajax({
        url: 'upload_file', 
        type: 'POST',
        data: formData,
        processData: false, 
        contentType: false,
        success: function(data) {
            console.log('Файл успешно отправлен!');
            console.log(data.text_file);
            textFile.innerHTML = "";
            for (let value of data.text_file) {
                let mySpan = document.createElement('span');
                mySpan.textContent = value;
                textFile.appendChild(mySpan);
                mySpan.addEventListener("mouseover", function() {
                    this.style.cssText = `
                        color: white;
                    `;
                })
                mySpan.addEventListener("mouseout", function() {
                    this.style.cssText = `
                        color: black;
                    `;
                });
                mySpan.addEventListener("click", function(event) {
                    $.ajax({
                        url: "upload_text",
                        type: "POST",
                        data: JSON.stringify({"span_text": this.textContent}),
                        processData: false,
                        contentType: false,
                        async: false,
                        success: function(data) {
                            console.log("Текст успешно отправлен")
                            console.log(data);
                            window.open("http://127.0.0.1:8000/dependency", "_blank");
                            event.preventDefault();
                        },
                        error: function(data) {
                            console.log("Произошла ошибка при отправке текста!")
                        }
                    });
                    
                });
                
            }
        },
        error: function(data) {
            console.log('Произошла ошибка при отправке файла!');
        }
    });
    
});

