import styles from "./NavItem.module.scss";
import { useRouter } from 'next/router'
import Link from "next/link";

export default function NavItem(props) {
  const router = useRouter()
  let active = router.pathname.indexOf(props.href) > -1 && props.href !== '/'
  return (
    <Link href={props.href}>
      <li className={"brand" in props ? styles.brand : (active ? styles.active : styles.box)}>
        {active ? <div className={styles.shadowblock}></div> : ''}
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
