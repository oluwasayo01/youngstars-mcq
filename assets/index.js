const handleClick = (elem) => {
  const testId = elem.value;
  localStorage.setItem("testId", testId);
  window.location.href = "quiz/";
};

// const addStory = () => {
//   window.location.href = "add-story/";
// };

const newQuestion = () => {
  const questionDiv = document.querySelector("#new-content");
  const newQuestionBtn = document.querySelector("#new-question-btn");
  newQuestionBtn.disabled = true;
  // const div = document.createElement('div')
  // div.appendChild('<h1>Yaay</h1>')
  const newQuest = `
    <div id="latest-question">
        <label for="quest">Question</label>
        <textarea name="quest" id="quest" cols="100" rows="1"></textarea>
        <h2>Options</h2>
        <ul class="options">
            <li class="option"><input id="option_1" type="text"/></li>
            <li class="option"><input id="option_2" type="text"/></li>
            <li class="option"><input id="option_3" type="text"/></li>
            <li class="option"><input id="option_4" type="text"/></li>
        </ul>
        <h2>Answer: <input id="correct_option"></h2>
        <button onclick="addQuestion()">Add</button>
        <button onclick="removeQuestion()" >Remove</button>
    </div>
    
    `;
  // console.log(questionDiv.innerHTML)
  questionDiv.insertAdjacentHTML("beforeend", newQuest);
};

const createStory = () => {
  const form = document.querySelector("#form");
  const heading = document.querySelector("#heading");
  const body = document.querySelector("#body");
  //   const newQuestionBtn = document.querySelector()
  if (
    !heading.value ||
    !body.value ||
    heading.value.length < 10 ||
    body.value.length < 100
  ) {
    alert("Enter valid heading and body texts. Story may be too short.");
  } else {
    const data = { heading: heading.value, body: body.value };
    // console.log(data)
    fetch("http://localhost:8000/mcq/create-story/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((resp) => {
        if (resp.status == 200) {
          form.id = "new-content";
          form.innerHTML = `
          <h1 id="new">${heading.value}</h1>
          <p>${body.value}</p>
          <button id="new-question-btn" onclick="newQuestion()">New Question</h1>
              `;
        }
        console.log(resp.status);
      })
      .catch((error) => console.log(error));
  }
};

const addQuestion = () => {
  const questions = document.querySelector(".questions");
  const heading = document.querySelector("#new").innerHTML;
  const question = document.querySelector("#quest").value;
  const option_1 = document.querySelector("#option_1").value;
  const option_2 = document.querySelector("#option_2").value;
  const option_3 = document.querySelector("#option_3").value;
  const option_4 = document.querySelector("#option_4").value;
  const correct_option = document.querySelector("#correct_option").value;
  console.log(question);
  console.log(option_1);

  const options = [option_1, option_2, option_3, option_4];
  const isPresent = options.includes(correct_option);

  if (
    !option_1 ||
    !option_2 ||
    !option_3 ||
    !option_4 ||
    !correct_option ||
    !quest
  ) {
    alert("make sure all options are");
  } else if (!isPresent) {
    alert("Correct option is not included in the options");
  } else {
    const data = {
      question,
      heading,
      option_1,
      option_2,
      option_3,
      option_4,
      correct_option,
    };
    console.log("data", data);

    fetch(`http://localhost:8000/mcq/create-question/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((resp) => {
        if (resp.status == 200) {
          alert("Question added to database");
          // document.querySelector('#latest-question')
          const newQuestionBtn = document.querySelector("#new-question-btn");
          newQuestionBtn.disabled = false;
        }
        console.log(resp.status);
      })
      .catch((error) => console.log(error));
  }
};

const deleteItem = (elem) => {
  const elemId = Number(elem.value);
  fetch(`http://localhost:8000/mcq/create-story/${elemId}/`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((res) => {
      window.location.href = '/'
    })
    .catch((error) => console.log(error));
};
