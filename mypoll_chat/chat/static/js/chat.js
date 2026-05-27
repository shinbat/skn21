// eventsource객체.addEventListenr("이벤트타입", 함수)

// DOMContentLoaded: HTML문서가 Load되면(HTML응답받아서 화면이 구성되는 시점)
//  - DOM Tree가 완성되면 발생하는 Event
document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');

    // 이벤트 처리함수: 파라미터로 event객체를 받을 수있다.
    // function handler(event: 발생한 Event 객체)
    chatForm.addEventListener('submit', (e) => {
        e.preventDefault(); 
        //발생한 Event의 기본 처리(handler)를 중단.
        // submit: form에서 전송

        const message = messageInput.value.trim(); //입력된 메세지 조회.
        if (!message) {
            alert("메세지를 입력하세요.");
            messageInput.focus();
            return;
        }
        // chotbot창에 전달한 메세지를 출력
        //  (출력할 메세지, "class 이름") 
        //  class 이름: user/ai-message 이것에 따라서 다른 스타일로 출력
        appendMessage(message, 'user-message');
        messageInput.value = '';
        // messageInput 활성(false)/비활성화(false)
        //비활성화-AI 응답이 오는 동안은 입력하지 못하게한다.
        toggleForm(true);

        // AI 응답을 담을 ElementNode(div)를 저장할 변수.
        let aiMessageElement = null;

        // EventSource: JS에서 SSE 지원 API
        // 객체 생성(요청 url)
        const eventSource = new EventSource(`/chat/stream/?message=${encodeURIComponent(message)}`);

        // EventSource에 Event Handler를 등록
        //  onmessage: 서버에서 메세지가 도착(message이벤트)할 때마다 호출되는 handler
        //  onerror: 서버와의 연결 에러가 발생하면 호출되는 handler
        eventSource.onmessage = (event) => {
            if (event.data === '[DONE]') {
                eventSource.close();
                toggleForm(false);
                return;
            }
            // LLM 응답 토큰을 받으면 처리.
            if (!aiMessageElement) {
                // 첫번째 토큰을 받으면 <div class='message ai-message'></div> 생성
                // 두번째 토큰 부터는 받은 토큰문자열을 element에 append
                aiMessageElement = appendMessage('', 'ai-message');
            }

            if (event.data.startsWith('[ERROR]')) {
                aiMessageElement.innerHTML += `<span style="color: red;">${event.data}</span>`;
                eventSource.close();
                toggleForm(false);
            } else {
                aiMessageElement.innerHTML += event.data;
            }
            chatBox.scrollTop = chatBox.scrollHeight;
        };

        eventSource.onerror = (err) => {
            console.error('EventSource 실패:', err);
            if (aiMessageElement) {
                aiMessageElement.innerHTML += `<span style="color: red;">[Error] 연결 실패</span>`;
            } else {
                appendMessage('<span style="color: red;">[Error] 연결 실패</span>', 'ai-message');
            }
            eventSource.close();
            toggleForm(false);
        };
    });

    function appendMessage(content, className) {
        const messageElement = document.createElement('div');//<div>
        messageElement.setAttribute("class", `message ${className}`);//<div class='message className'>
        messageElement.innerHTML = content;//<div class='message className'>content</div>
        chatBox.appendChild(messageElement);//chatbot 창에 마지막 자식 노드로 추가.
        chatBox.scrollTop = chatBox.scrollHeight; // 스크롤을 아래로 내린다.
        return messageElement;
    }

    function toggleForm(disabled) {
        // elementNode.disabled: 노드를 활성/비활성화 시키는 속성.
        messageInput.disabled = disabled;
        sendButton.disabled = disabled;
        if (!disabled) {// 활성화 되면 포커스를 메세지 입력으로 옮긴다.
            messageInput.focus();
        }
    }
});
