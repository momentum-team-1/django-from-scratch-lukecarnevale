document.querySelector('.card-container').addEventListener('click', (event) => {
  event.preventDefault()
  document.querySelector('.card-container').classList.toggle('flipped')
})