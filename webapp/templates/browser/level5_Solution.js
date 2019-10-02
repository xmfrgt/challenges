var connection = indexedDB.open('level9', 1)

connection.onsuccess = (e) => {
  var database = e.target.result;
  var transaction = database.transaction(["level9"], "readwrite");
  var objectStore = transaction.objectStore("door");
  var request = objectStore.put({id:"1", isLoggedIn: true});

  request.onsuccess = (e) => {
    console.log('Changed isLoggedIn')
  }
  request.onerror = (e) => {
    console.log('Error changing isLoggedIn')
  }
}