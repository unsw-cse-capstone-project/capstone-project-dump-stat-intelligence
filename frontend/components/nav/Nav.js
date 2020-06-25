import styles from "./Nav.module.scss";
import Brand from "../icons/Brand";
import Explore from "../icons/Explore";
import Cookbook from "../icons/Cookbook";
import Create from "../icons/Create";
import Settings from "../icons/Settings";
import Pantry from "../icons/Pantry";
import NavItem from "./NavItem";

export default function Nav() {
  return (
    <nav className={styles.nav}>
      <ul>
        <NavItem icon={<Brand />} brand={true} href="/" />
        <NavItem icon={<Explore />} name={"Explore"} href="/explore" />
        <NavItem icon={<Pantry />} name={"Pantry"} href="/pantry" />
        <NavItem icon={<Cookbook />} name={"Cookbook"} href="/cookbook" />
        <NavItem icon={<Create />} name={"Create"} href="/recipe/create" />
        <NavItem icon={<Settings />} name={"Settings"} href="/settings" />
      </ul>
    </nav>
  );
}
