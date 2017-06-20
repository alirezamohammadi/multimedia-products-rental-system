"use strict"

function numberOfDisksAjaxRequest() {
    let id = document.getElementById("id").value;
    let xhttp = new XMLHttpRequest();
    let disk;
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {

            disk = JSON.parse(this.responseText);
            if (disk.message != "None") {
                let message=`
                    <div class="col-md-6 col-md-offset-3">
                        <div class="alert alert-danger">
                            ${disk.message}
                        </div>
                    </div>`

                document.getElementById("demo").innerHTML = message;
            }
            else {
                let table = `
                <div class="container">
                    <table class="table table-hover">
                        <thead>
                        <tr>
                            <th>شناسه</th>
                            <th>عنوان</th>
                            <th>ژانر</th>
                            <th>تعداد</th>
                            <th>نوع</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>${disk.id}</td>
                            <td>${disk.title}</td>
                            <td>${disk.genre}</td>
                            <td>${disk.number}</td>
                            <td>${disk.type}</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col-md-6 col-md-offset-3">
                    <form method="POST">
                        <input type="number" class="form-control" name="disk_numbers" min="0" value="${disk.number}" required /><br />
                        <input type="submit" class="form-control btn btn-danger" value="به روز رسانی" />
                    </form>
                </div>
                `
                document.getElementById("demo").innerHTML = table;
            }
        }
    };
    xhttp.open("POST", "number_of_disks", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("title_id=" + id);
}