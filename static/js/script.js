
function currentTime(){
    let date = new Date();
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();
    let session = "AM";


    if(hh == 0){
        hh = 12
    }

    if(hh > 12){
        hh = hh - 12;
        session = "PM";
    }

    hh = (hh < 10) ? "0" + hh : hh;
    mm = (mm < 10) ? "0" + mm : mm;
    ss = (ss < 10) ? "0" + ss : ss;

    let time = hh + ":" + mm + ":" + ss + " " + session;

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
