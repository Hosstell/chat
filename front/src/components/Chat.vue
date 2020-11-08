<template>
  <div>

    <h5> Чат </h5>
    <v-card class="mt-3">
      <v-card-text>
        <v-row class="text-left" style="height: 600px; overflow: auto;">
          <v-list class="ml-2">
            <v-list-item
              v-for="(message, i) in messages"
              :key="i"
              class="message-border ml-3 pl-2 mb-2"
              style="height: 60px"
            >
              <v-list-item-content class="p-1">
                <div>
                  <v-icon
                    v-text="'mdi-account'"
                    :color="message.user.sex === 'M' ? 'blue' : 'pink'"
                    class="pb-1"
                  />
                  {{ message.user.name }}
                </div>
                <div>
                  <v-list-item-title v-text="message.text"></v-list-item-title>
                </div>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-row>
      </v-card-text>
    </v-card>

    <v-card class="mt-1">
      <v-card-text>
        <v-row>
          <v-col cols="11" class="p-0 pl-4">
            <v-text-field
              v-model="messageText"
              outlined
              placeholder="Введите сообщение..."
              dense
              clearable
              hide-details
            />
          </v-col>
          <v-col cols="1" class="p-0">
            <v-btn
              elevation="2"
              icon
              outlined
              @click="sendMessage"
            >
              <v-icon v-text="'mdi-send'" />
            </v-btn>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

  </div>
</template>

<script>
  import {socket} from './socket'

  export default {
    name: "Chat",
    data: () => ({
      messages: [],
      messageText: ''
    }),
    methods: {
      getMessage(message) {
        this.messages.push(message)
      },
      sendMessage() {
        socket.sendMessage(this.messageText)
        this.messageText = ''
      }
    },
    mounted() {
      socket.setMessageHandler(this.getMessage)
    }
  }
</script>

<style scoped>
  .message-border {
    border-left: 2px solid #bababa;
  }

</style>