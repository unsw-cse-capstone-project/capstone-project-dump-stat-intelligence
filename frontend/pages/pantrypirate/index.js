import Link from 'next/link'
import { useSelector } from 'react-redux';

import { removeUser } from "../../lib/utils/localstorage";

export default function Home() {
  const sayings = [
    "Yarrhhhhggg, these 'ere cados 🥑 do be lookin' ripe t' eat",
    "Grrrrr, I be wonderin' what eye can cook wit' these 'ere coconuts 🥥",
    "Yohoho, it be high time for a snack, what can eye be cookin' with me ripe cherries? 🍒",
    "Argghhh I be sick o' boiled taters... 🥔 what can I do wit' 'em instead",
    "Ayeee, if only I could find a recipe t' use me broccolini 🥦 and carrots 🥕 t'gether..."
  ]
  
  let isLoggedIn = useSelector(state => state.auth.isLoggedIn)
  
  function rand(cieling) {
    return Math.floor(Math.random() * cieling);
}

  function toggle(id) {
    document.getElementById(id).classList.toggle("is-active")
  }
  
  return (
    <div className="hero is-fullheight">
      <div className="hero-body">
        <div className="container">
          <div>
            <img src="/logo.svg" style={{ width: 180 + "px" }} />
            <h1 className="title">Pantry Pirate</h1>
          </div>
          <h1 className="title is-1">Plunder Your Pantry!</h1>
          <h3 className="subtitle is-4">
            {sayings[rand(sayings.length)]}
          </h3>
          {isLoggedIn ? 
            <Link href='/explore'>
              <button className="button is-primary">Start Plundering</button>
            </Link>      
          : 
            <div className="buttons">
              <button onClick={() => {toggle('auth-login')}} className="button is-primary">Log In</button>
              <button onClick={() => {toggle('auth-register')}} className="button is-secondary">Sign Up</button>
            </div>
          }
        </div>
      </div>
    </div>
  );
}
