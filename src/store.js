import { writable } from 'svelte/store'

function createEntries() {
  let localEntries = window.localStorage.getItem('entries')
  if (localEntries == null) {
    localEntries = []
  } else {
    localEntries = JSON.parse(localEntries)
  }

  const { subscribe, set, update } = writable(localEntries)

  return {
    subscribe,
    set: (val) => {
      set(val)

      window.localStorage.setItem('entries', JSON.stringify(val))
    },
    update: (cb) => {
      update((val) => {
        val = cb.call(val)
        window.localStorage.setItem('entries', JSON.stringify(val))
        return val
      })
    }
  }
}

export const entries = createEntries()

export const drawingStarted = writable(false)
export const drawingEnded = writable(false)
