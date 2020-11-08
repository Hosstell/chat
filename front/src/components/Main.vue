<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="3">
        <user-list />
      </v-col>

      <v-col cols="9" class="p-2">
        <Chat />
      </v-col>
    </v-row>

    <personal-info-dialog @enter="setInfo" ref="info"/>
  </v-container>
</template>

<script>
  import UserList from "./UserList";
  import Chat from "./Chat";
  import PersonalInfoDialog from "./PersonalInfoDialog";
  import {socket} from './socket'

  export default {
    name: 'Main',
    components: {PersonalInfoDialog, Chat, UserList},
    data: () => ({

    }),
    methods: {
      setInfo({name, sex}) {
        socket.sendMyData({name, sex})
      },
      getMyData({name}) {
        if (!name.length) {
          this.$refs.info.openDialog()
        }
      }
    },
    mounted() {
      socket.connect()
      socket.setGetMyDataHandler(this.getMyData)
    }
  }
</script>
