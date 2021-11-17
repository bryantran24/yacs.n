import { effect, reactive } from 'vue'

interface X {
  currentSemester: string
  courseSelection: Record<string, string[]>
  possibilityIndex: number
  colors: string[]
}

const LocalStorage = (key: string, defaultValue: any): any => {
  const data = reactive({})

  Object.assign(
    data,
    (localStorage[key] && JSON.parse(localStorage[key])) || defaultValue
  )

  effect(() => (localStorage[key] = JSON.stringify(data)))

  return data
}

export default (function (): X {
  return LocalStorage('yacs', {
    currentSemester: '',
    courseSelection: {},
    possibilityIndex: 0,
    colors: []
  })
})()
