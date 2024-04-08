
function currentTime(){
    let date = new Date();
    let hours = date.getHours();
    let minutes = date.getMinutes();
    let seconds = date.getSeconds();
    let session = "AM";


    if(hours == 0){
        hours = 12
    }

    if(hours > 12){
        hours = hours - 12;
        session = "PM";
    }

    hours = (hours < 10) ? "0" + hours : hours;
    minutes = (minutes < 10) ? "0" + minutes : minutes;
    seconds = (seconds < 10) ? "0" + seconds : seconds;

    let time = hours + ":" + minutes + ":" + seconds + " " + session;

    document.getElementById("clock").innerText = time; 
    let t = setTimeout(function(){ currentTime() }, 1000);

}

currentTime();

// Task list

let submitBtn = document.getElementById("submit");
let input = document.getElementById("inputBar");
let ul = document.getElementById("taskList");
let item = document.getElementsByTagName("li");

function inputLength() {
    return input.value.length;
}
function listLength(){
    return item.length;
}


function createListItem() {
    
    // Creates an element li to add to the list
    
    let li = document.createElement("li")
    li.appendChild(document.createTextNode(input.value));
    ul.appendChild(li);
    input.value = "";

    // Completed Item on list
   
    function taskComplete() {
        li.classList.toggle("finished");
    }

    li.addEventListener("click", taskComplete)

    // Delete Button

    let deleteBtn = document.createElement("button");
    deleteBtn.appendChild(document.createTextNode("X"));
    li.appendChild(deleteBtn);
    deleteBtn.addEventListener("click", deleteTaskItem);

    function deleteTaskItem() {
        li.classList.add("delete")
    }
}

// Function to add a task after clicking

function addAfterClick() {
    if (inputLength() > 0) {
        createListItem();
    }
}

// Function to add a task after hitting Enter

function addAfterKeyPress(event) {
	if (inputLength() > 0 && event.keyCode === 13) { 
		createListElement();
	} 
}

submitBtn.addEventListener("click",addAfterClick);

input.addEventListener("keypress", addAfterKeyPress);
