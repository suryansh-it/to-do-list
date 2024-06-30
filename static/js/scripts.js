// funcction t handke compeletion toggle

function toggleComplete(todoId){
    fetch('/toggle/${toggleId}' , 
        {method:'POST'})

        .then(response =>{
            if(response.ok) 
                {window.location.reload();  // Reload page to reflect changes
            }
        })

        .catch(error => {
            console.error("error toggling todo completion:" , error);
        });
    }

    //function to handle deletion

    function deleteTodo(todoId){
        fetch('/delete/${todoId}' ,{
            method:"POST"
        })
        .then(response =>{
            if(response.ok)
            {window.location.reload();  // Reload page to reflect changes
        }
        })
        .catch(error => {
            console.error("error deleting todo:", error);
        });
    }


