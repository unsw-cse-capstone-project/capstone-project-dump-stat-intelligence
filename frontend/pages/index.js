import Link from 'next/link'


export default function Home() {
  let isLoggedIn = true
  
  
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
            Yarrhhhhggg, these 'ere cados 🥑 do be lookin' ripe t' eat
          </h3>
          {isLoggedIn ? 
            <Link href='/explore'>
              <button className="button is-primary">Start Plundering</button>
            </Link>      
          : 
            <div className="buttons">
              <button onClick={() => {toggle('auth-register')}} className="button is-primary">Sign Up</button>
              <button onClick={() => {toggle('auth-login')}} className="button is-secondary">Log In</button>
            </div>
          }
        </div>
      </div>
    </div>
  );
}
