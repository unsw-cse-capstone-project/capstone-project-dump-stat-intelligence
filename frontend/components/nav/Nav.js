import styles from "./Nav.module.scss";
import Brand from "../icons/Brand";
import Explore from "../icons/Explore";
import Cookbook from "../icons/Cookbook";
import Create from "../icons/Create";
import Settings from "../icons/Settings";
import Pantry from "../icons/Pantry";
import User from "../icons/User";
import NavItem from "./NavItem";
import NavLogin from "./NavLogin";
import Login from "../authentication/Login";
import Logout from "../authentication/Logout";
import Register from "../authentication/Register";

export default function Nav() {
  //Get all the modal backgrounds to close the modal
  /*let modal_bgs = document.getElementsByClassName("modal-background")
  for (var i = 0; i < modal_bgs.length; i++) {
    modal_bgs[i].addEventListener('click', () => {modal_bgs[i].parentElement.classList.toggle("is-active")});
  }*/
  return (
    <>
      
      <nav className={styles.nav}>
        <div className={styles.upperNav}>
          <ul>
            <NavItem icon={<Brand />} brand={true} href="/" />
            <NavItem icon={<Explore />} name={"Explore"} href="/explore" />
            <NavItem icon={<Pantry />} name={"Pantry"} href="/pantry" />
            <NavItem icon={<Cookbook />} name={"Cookbook"} href="/cookbook" />
            <NavItem icon={<Create />} name={"Create"} href="/recipe/create" />
          </ul>
        </div>
        <div className={styles.lowerNav}>
          <ul>
            <NavLogin icon={<User />} name={"Login / Register"}/>
            <NavItem icon={<Settings />} name={"Settings"} href="/settings" />
          </ul>
        </div>
      </nav>
      <Login login="auth-login" register="auth-register"/>
      <Logout logout="auth-logout"/>
      <Register login="auth-login" register="auth-register"/>

    </>
  );
}
