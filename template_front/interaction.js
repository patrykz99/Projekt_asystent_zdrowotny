const messagesBox = document.getElementById('display-box');
const form = document.querySelector('.bottom');
const input = document.getElementById('message-prompt');
const clearChatButton = document.getElementById('refresh')
let state = true;

form.addEventListener('submit', async(x)=>{
    x.preventDefault();

    let message = input.value;
    if (message.trim() !== "") {
        if (state) {
            addMess('user',message);
        } else {
            addMess('bot',message);
        }
        
        state = !state; 
      }
    
    input.value = "";


});

clearChatButton.addEventListener('click',()=>{
    messagesBox.innerHTML = "";
})

function addMess(sender,text){
    const outputArea = document.createElement('div');
    const senderType = document.createElement('span')
    const messageDisplay = document.createElement('div');

    outputArea.classList.add('output-area',sender);

    senderType.classList.add('sender-type')
    if (sender === 'user'){
        senderType.textContent = "Me " 
    }else{
        senderType.textContent = "Assistant "
    };

    messageDisplay.classList.add('message-display',sender);
    messageDisplay.textContent = text;
    
    outputArea.appendChild(senderType);
    outputArea.appendChild(messageDisplay);


    messagesBox.appendChild(outputArea);
    messagesBox.scrollTop = messagesBox.scrollHeight;
}

