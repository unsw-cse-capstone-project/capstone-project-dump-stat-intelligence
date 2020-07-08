import styles from "./Edit.module.scss";

import Create from "../icons/Create";
import Editor from "./Editor";

export default function EditButton() {
    const playHoverPop = () => {
        let audio = document.getElementById(`pop1`);
        audio.play();
    }
    return <>
        <div onMouseEnter={playHoverPop} onClick={() => document.getElementById("editor").classList.toggle(styles.editorShow)} className={styles.editButton}>
            <div className={styles.iconBox}>
                <Create/>
            </div>


        </div>
        <Editor/>
        <audio id={`pop1`}>
          <source src={`/audio/pop1.mp3`} />
        </audio>
    </>
}