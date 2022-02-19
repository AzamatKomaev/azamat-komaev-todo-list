function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


const updateTask = (taskId) => {
    const csrftoken = getCookie('csrftoken');
    axios.patch(`http://127.0.0.1:8000/tasks/${taskId}/update`, {}, {
        headers: {
            "X-CSRFToken": csrftoken
        }
    })
        .then((response) => {
            if (response.data.status === 200) {
                location.reload()
                return ;
            }
            alert("some problem")
        })
        .catch((error) => {
            console.log(error)
            alert("You cant do it!!")
        })
}

const redirectToUserTasks = () => {
    const userTasksInput = document.getElementById('task-user-input')

    if (userTasksInput.value) {
        window.location.href = `http://127.0.0.1:8000/tasks/?sort_type=filter_by_user&user_username=${userTasksInput.value}`
        return ;
    }
    alert('The input cant be empty!')
    return null;
}

