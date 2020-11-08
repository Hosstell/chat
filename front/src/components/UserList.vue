<template>
  <div>

    <h5> Участники </h5>
    <v-card>
      <v-card-text class="p-0">
        <v-list dense>
          <v-list-item
            v-for="(user, i) in users"
            :key="i"
          >
            <v-list-item-icon>
              <v-icon
                v-text="'mdi-account'"
                :color="user.sex === 'M' ? 'blue' : 'red'"
              />
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="user.name"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
  import {socket} from "./socket";

  export default {
    name: "UserList",
    data: () => ({
      users: []
    }),
    methods: {
      setUserList(userList) {
        console.log('userList', userList)
        this.users = userList
      }
    },
    mounted() {
      socket.setUserListHandler(this.setUserList)
    }
  }
</script>

<style scoped>

</style>