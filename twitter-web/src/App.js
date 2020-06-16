import React from 'react';
import logo from './logo.svg';
import './App.css';

import {TweetsComponent} from './tweets'

// function loadTweets(callback){
//   const xhr = new XMLHttpRequest()
//   const method= 'GET'
//   const url="http://localhost:8000/api/tweets/"
//   const responseType="json"
//
//   xhr.responseType=responseType
//   xhr.open(method, url)
//   xhr.onload = function() {
//     callback(xhr.response, xhr.status)
//   }
//   xhr.onerror= function(e) {
//     console.log(e)
//     callback({"message": "the request was an error"}, 400)
//   }
//   xhr.send()
// }
//
// function TweetsList(props) {
//   const [tweets, setTweets] = useState([])
//
//   useEffect(() => {
//     const mycallback= (response, status) => {
//       if(status === 200){
//       // const tweetItems = [{"content":123}, {"content":"Hello World"}]
//       setTweets(response)
//     }
//
//     }
//     loadTweets(mycallback)
//     const tweetItems = [{"content":123}, {"content":"Hello World"}]
//     setTweets(tweetItems)
//   }, [])
//
//
// function ActionBtn(props){
//   const {tweet,action} = props
//   const className = props.className ? props.className : 'btn btn-primary btn-sum'
//   return action.type === 'like' ? <button className={className}> {tweet.likes} Likes</button>:null
// }
//
//
// function Tweet(props) {
//   const {tweet}=props
//   const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
//   return <div className={className}>
//   <p>{tweet.id} - {tweet.content}</p>
//   <div className='btn btn-group'>
//   <ActionBtn tweet={tweet} action={{type : "like"}}/>
//   </div>
//   </div>
// }
//
// function App() {
//   const [tweets, setTweets] = useState([])
//
// useEffect(() => {
//   const mycallback= (response, status) => {
//     if(status === 200){
//     // const tweetItems = [{"content":123}, {"content":"Hello World"}]
//     setTweets(response)
//   }
//
//   }
//   loadTweets(mycallback)
//   const tweetItems = [{"content":123}, {"content":"Hello World"}]
//   setTweets(tweetItems)
// }, [])
//    return tweets.map((item,index)=>{
//      return <Tweet tweet={item} className='my-5 py-5 border bg-white text-dark' key={index-item.id}/>
//    })
//  }
//

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
        <TweetsComponent/>
        </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
