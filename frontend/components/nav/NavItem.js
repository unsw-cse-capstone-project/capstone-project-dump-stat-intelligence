import styles from "./NavItem.module.scss";

import Link from "next/link";

export default function NavItem(props) {
  return (
    <Link href={props.href}>
      <li className={"brand" in props ? styles.brand : styles.box}>
        {props.icon}
        {"brand" in props ? (
          ""
        ) : (
          <span className={styles.tag}>{props.name}</span>
        )}
      </li>
    </Link>
  );
}
