import styles from "./Nav.module.scss";
import Brand from "../icons/Brand";
import Explore from "../icons/Explore";
import Cookbook from "../icons/Cookbook";
import Create from "../icons/Create";
import Settings from "../icons/Settings";
import User from "../icons/User";
import NavItem from "./NavItem";
import NavLogin from "./NavLogin";
import Login from "../authentication/Login";
import Logout from "../authentication/Logout";
import Register from "../authentication/Register";
import ExpiryEdit from "../Pantry/ExpiryEdit";

import { useSelector } from "react-redux";

export default function Nav() {
  let isLoggedIn = useSelector((state) => state.auth.isLoggedIn);

  return (
    <>
      <nav className={styles.nav}>
        <div className={styles.upperNav}>
          <ul>
            <NavItem popSound="2" icon={<Brand />} brand={true} href="/" />
            <NavItem
              popSound="1"
              icon={<Explore />}
              name={"Explore"}
              href="/explore"
            />
            {/* <NavItem icon={<Pantry />} name={"Pantry"} href="/pantry" /> */}
            <NavItem
              popSound="2"
              restricted={"auth-login"}
              icon={<Cookbook />}
              name={"Cookbook"}
              href="/cookbook"
            />
            <NavItem
              popSound="3"
              restricted={"auth-login"}
              icon={<Create />}
              name={"Create"}
              href="/recipe/create"
            />
          </ul>
        </div>
        <div className={styles.lowerNav}>
          <ul>
            <NavLogin
              popSound="2"
              login="auth-login"
              logout="auth-logout"
              isLoggedIn={isLoggedIn}
              icon={<User />}
            />
            <NavItem
              popSound="5"
              restricted={"auth-login"}
              icon={<Settings />}
              name={"Settings"}
              href="/settings"
            />
          </ul>
        </div>
      </nav>
      <Login login="auth-login" register="auth-register" />
      <Logout logout="auth-logout" />
      <Register login="auth-login" register="auth-register" />
      <ExpiryEdit/>
    </>
  );
}
