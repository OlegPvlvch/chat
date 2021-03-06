const chatSocket = new WebSocket(
	'ws://' + window.location.host
);

chatSocket.onmessage = function(e) {
	const data = JSON.parse(e.data);
	document.querySelector('#chat-log').value += (data.sender + ' : ' + data.message + '\n');
};

chatSocket.onclose = function(e) {
	console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
	if (e.keyCode === 13) {  // enter, return
		document.querySelector('#chat-message-submit').click();
	}
};

document.querySelector('#chat-message-submit').onclick = function(e) {
	const messageInputDom = document.querySelector('#chat-message-input');
	const message = messageInputDom.value;
	if(message){
		chatSocket.send(JSON.stringify({
			'message': message,
			//'sender' : 'Client'
		}));
	}
	messageInputDom.value = '';
};