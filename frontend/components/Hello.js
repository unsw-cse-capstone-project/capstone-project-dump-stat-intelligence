import styles from "./Hello.module.scss";

export default function Yeet() {
  return (
    <div className={styles.hello}>
      <p>
        This component is styled with its own module and by the global styles
      </p>
    </div>
  );
}
