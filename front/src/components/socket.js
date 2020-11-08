class ChatSocket {
  constructor(url) {
    this.url = 'ws://'+ url

    this.socket = undefined
    this.messageHandler = () => {}
    this.userListHandler = () => {}
    this.getMyDataHandler = () => {}
  }

  setMessageHandler(newMessageHandler) {
    this.messageHandler = newMessageHandler
  }

  setUserListHandler(newUserListHandler) {
    this.userListHandler = newUserListHandler
  }

  setGetMyDataHandler(newGetMyDataHandler) {
    this.getMyDataHandler = newGetMyDataHandler
  }

  connect() {
    this.socket = new WebSocket(this.url)

    this.socket.onmessage = this.handlerQuery.bind(this)

    this.socket.onopen = () => {
      this.getMyData()
      this.sendQuery('online', {})
    }
  }

  handlerQuery(event) {
    let data = JSON.parse(event.data)
    console.log(data)

    if (data.type === 'user_list') {
      this.userListHandler(data.message)
    }

    if (data.type === 'message') {
      this.messageHandler(data.message)
    }

    if (data.type === 'my_data') {
      this.getMyDataHandler(data.message)
    }
  }

  sendMyData(data) {
    this.sendQuery('myData', data)
  }

  sendMessage(message) {
    this.sendQuery('message', message)
  }

  getMyData() {
    this.sendQuery('getMe', {})
  }

  sendQuery(type, data) {
    this.socket.send(JSON.stringify({ type, data }))
  }
}

const socket = new ChatSocket('localhost:8000/ws/chat/')
export {socket}

