function UserBooks() {
    var token = localStorage.getItem('userToken');
    var tbody = document.getElementById('books');
    var html ='';
    fetch(`http://127.0.0.1:8000/userbooks/?usertoken=${token}`)
        .then(res=>res.json())
        .then(jRes=>{
            for(var i = 0;i<jRes.length;i++){
                var t = jRes[i].title;
                var bt = jRes[i].book_type;
                var fv = jRes[i].favbook;
                var des = jRes[i].description;
                if(fv === true){
                    var icon = '<i class="fa fa-heart text-danger" style="font-size: 20px"></i>'
                }
                else{
                    var icon = '<i class="fa fa-heart" style="font-size: 20px"></i>'
                }
                html+=`<tr>
                       <td>${t}</td>
                        <td>${bt}</td>
                 
                         <td>${icon}</td>
                          <td>${des}</td>
                          <td><i class="fa fa-trash text-danger" 
                          onclick="DeleteBook(${jRes[i].id})" style="font-size: 20px"></i>
                          &nbsp;&nbsp;
                         <a href='/update_book/${jRes[i].id}'><i class="fa fa-pencil-square text-info" style="font-size: 20px"></i>
                         </a>
                          </td>
                      </tr>`
            }
            tbody.innerHTML = html
        })
}

function DeleteBook(book_id){
    fetch(`http://127.0.0.1:8000/book_delete/${book_id}`,{
        method:"DELETE",
        headers:{
            Authorization: 'jwt '+localStorage.getItem('userToken')
        }
    })
    window.location = '/home'



}



window.onload = UserBooks;