import styles from "./NavItem.module.scss";
import { useRouter } from "next/router";
import Link from "next/link";
import { useSelector, useDispatch } from "react-redux";
import { new_next } from "../../lib/redux/actions/authAction"

export default function NavItem(props) {
  const router = useRouter();
  const dispatch = useDispatch();
  let isLoggedIn = useSelector((state) => state.auth.isLoggedIn);
  let active = router.pathname.indexOf(props.href) > -1 && props.href !== "/";
  function forceLogin() {
    document.getElementById(props.restricted).classList.add("is-active");
    document.getElementById(props.restricted + "-alert").innerHTML =
      "You must log in before you can use this feature.";
    document
      .getElementById(props.restricted + "-alert")
      .classList.add(styles.show);
    dispatch(new_next(props.href));
  }

  const playHoverPop = () => {
    let audio = document.getElementById(`pop-${props.popSound}`);
    audio.play();
  };

  return (
    <>
      <div onMouseEnter={() => playHoverPop()}>
        {props.restricted && !isLoggedIn ? (
          <li onClick={forceLogin} className={styles.box}>
            {props.icon}
            <span className={styles.tag}>{props.name}</span>
          </li>
        ) : (
          <Link href={props.href}>
            <li
              className={
                "brand" in props
                  ? styles.brand
                  : active
                  ? styles.active
                  : styles.box
              }
            >
              {active ? <div className={styles.shadowblock}></div> : ""}
              {props.icon}
              {"brand" in props ? (
                ""
              ) : (
                <span className={styles.tag}>{props.name}</span>
              )}
            </li>
          </Link>
        )}
      </div>
      <audio id={`pop-${props.popSound}`}>
        <source src={`/audio/pop${props.popSound}.mp3`} />
      </audio>
    </>
  );
}
