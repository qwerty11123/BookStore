function Add_Update_Book(e,urlname,method,BookId=0) {
        e.preventDefault()
        var cat_id = document.getElementById('catId').value;
        console.log(cat_id)
        var title = document.getElementById('title').value;
        var book_type = document.getElementById('book_type').value;
        var des = document.getElementById('des').value;
        var fav = document.getElementById('fav').checked;
        var formData = new FormData()
        formData.set('title',title)
        formData.set('category',cat_id)
        formData.set('book_type',book_type)
        formData.set('description',des)
        formData.set('favbook',fav)
        if(BookId !== 0){
            var endpoint = `http://127.0.0.01:8000/${urlname}/${BookId}/`
        }
        else{
            var endpoint = `http://127.0.0.01:8000/${urlname}/`
        }
        fetch(endpoint,{
            method:method,
            headers:{
                Authorization:'jwt '+localStorage.getItem('userToken')
            },
            body:formData
        })
            .then(res=>res.json())
            .then(jRes=>{
                if(method === 'POST'){
                    alert(`${jRes.book.title} added SuccessFully`)
                }
                else{
                    alert(`${jRes.title} updated SuccessFully`)
                }
                window.location = '/home'
            })




    }