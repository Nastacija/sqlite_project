addEventListener('DOMContentLoaded', doc_loaded => { 
  console.log('hello');

  const addSent = document.getElementById('sent');
  const sentBut = document.getElementById('click1');

  const morphWord = document.getElementById('show_word');
  const morphBut = document.getElementById('click2');
  const morphemes = document.getElementById('morph')

  const addWord = document.getElementById('word');
  const wordBut = document.getElementById('click3');
  const info = document.getElementById('word_exists')

  // Обработчик для предложений
  sentBut.addEventListener('click', function(event) {
    const text = addSent.value;
    const jsonData = { sentence: text };
    fetch('/insert_sent', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => {response.json()})
    .then(console.log(jsonData))
  })

  // Обработчик для разбора слова по составу
  morphBut.addEventListener('click', function(event) {
    const text = morphWord.value;
    const jsonData = { word: text };
    fetch('/get_morph', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
      })
      .then(console.log(jsonData))
      .then(response => response.json())
      .then(data => morphemes.innerText = data.answer)
    })

  // Обработчик для слов
  wordBut.addEventListener('click', function(event) {
    const text = addWord.value;
    const jsonData = { word: text };
    fetch('/insert_word', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(console.log(jsonData))
    .then(response => response.json())
    .then(data => info.innerText = data.reaction)
  })
})
