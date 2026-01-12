let count=1;
document.getElementById('add').addEventListener('click', function() {
        const newItem = document.getElementById('item').value;
        if (newItem.trim() === '') return;
        const li = document.createElement('li');
        li.textContent = newItem+" "+count;
        count+=1;
        document.getElementById('ul-list').appendChild(li);
        document.getElementById('item').value = '';
        
      });