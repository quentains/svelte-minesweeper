const backend = "127.0.0.1"

export default {
  async new_game(width, height) {
    return fetch(`${backend}/new_game?width=${width}&height=${height}`)
    .then(response => response.json())
    .then((out) => {
      console.log('Checkout this JSON! ', out);
    })
    .catch(err => { throw err });
  }
}
