const backend = "http://0.0.0.0:8000"

export default {
  async new_game(width, height) {
    return fetch(`${backend}/new_game/?width=${width}&height=${height}`)
    .then(response => response.json())
    .catch(err => { throw err });
  }
}
