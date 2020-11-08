<template>
  <v-dialog
    v-model="dialog"
    persistent
    max-width="500"
  >
    <v-form v-model="valid">
      <v-card>
        <v-card-title>
          Введите Ваши данные
        </v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="12">
              <v-text-field
                label="Никнейм"
                v-model="name"
                outlined
                :rules="[notNull]"
              />
            </v-col>
            <v-col cols="12">
              <v-select
                label="Пол"
                v-model="sex"
                :items="sexItems"
                outlined
                :rules="[notNull]"
              >
              </v-select>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions>
          <v-spacer/>
          <v-btn text :disabled="!valid" @click="enter">
            Войти в чат
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-dialog>
</template>

<script>
  export default {
    name: "PersonalInfoDialog",
    data: () => ({
      dialog: false,
      valid: true,
      name: '',
      sex: undefined,
      notNull: text => !!text || 'Поле должно быть заполнено',
      sexItems: [
        'Мужской',
        'Женский'
      ]
    }),
    methods: {
      openDialog() {
        this.dialog = true
      },
      closeDialog() {
        this.dialog = false
      },
      enter() {
        this.$emit('enter', {
          name: this.name,
          sex: this.sex
        })
        this.closeDialog()
      }
    }
  }
</script>

<style scoped>

</style>