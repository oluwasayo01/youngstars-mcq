function handleClick(elem) {
    
}


const addStory = () => {
    window.location.href = '/add-story'
}

const newQuestion = () => {
    const questionDiv = document.querySelector('#form')
    // const div = document.createElement('div')
    // div.appendChild('<h1>Yaay</h1>')
    const newQuest = `
    <div>
        <label for="heading">Title</label>
        <textarea name="heading" id="" cols="100" rows="1"></textarea>
        <h2>Options</h2>
        <ul class="options">
            <li class="option"><input name="option_1" type="text"/></li>
            <li class="option"><input name="option_2" type="text"/></li>
            <li class="option"><input name="option_3" type="text"/></li>
            <li class="option"><input name="option_4" type="text"/></li>
        </ul>
        <h2>Answer: <input name="correct_option"></h2>
        <button onclick="addQuestion()">Add</button>
        <button onclick="removeQuestion()" >Remove</button>
    </div>
    
    `
    // console.log(questionDiv.innerHTML)
    questionDiv.innerHTML = newQuest

}


const addQuestion = () => {
    const questions = document.querySelector('.questions')

}


const createStory = () => {
    const heading = document.querySelector("#heading")
    const body = document.querySelector("#body")
    if (!heading.value || !body.value || heading.value.length < 10 || body.value.length < 100) {
        alert("Enter valid heading and body texts. Story may be too short.")
    } else {
        const data = {heading, body}
        fetch('http://localhost:8000/mcq/create-story', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        })
        .then(resp => resp.data)
        .then(res => {
            if (res.status == 200) {
                console.log(success)
            }
        }).catch( error => console.log(error))

    }
}