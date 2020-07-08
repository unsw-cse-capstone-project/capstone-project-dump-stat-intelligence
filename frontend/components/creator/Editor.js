import styles from "./Edit.module.scss";
import React, { useState } from 'react';

export default function Editor() {
    const [active, setActive] = useState(0)
    function chooseTab(num) {
        document.getElementById(`editBox${active}`).classList.remove(styles.showBox)
        setActive(num);
        document.getElementById(`editBox${num}`).classList.add(styles.showBox)
    }
    return <>
        <div id="editor" className={styles.editor}>
            <div className="tabs">
                <ul>
                    <li onClick={() => chooseTab(0)} className={active === 0 ? "is-active" : ""}><a>General</a></li>
                    <li onClick={() => chooseTab(1)} className={active === 1 ? "is-active" : ""}><a>Ingredients</a></li>
                    <li onClick={() => chooseTab(2)} className={active === 2 ? "is-active" : ""}><a>Method</a></li>
                </ul>
            </div>
            <div id="editBox0" className={`${styles.editBox} ${styles.showBox}`}>
                <form className="form">
                    <div className="field control">
                        <label className="label">Title</label>
                        <input name="title" className="input" type="text"/>
                    </div>
                    <div className="field control">
                        <label className="label">Cook time</label>
                        <input name="cook_time" className="input" type="text"/>
                    </div>
                    <div className="field control">
                        <label className="label">Image URL</label>
                        <input name="cook_time" className="input" type="text"/>
                    </div>
                </form>
            </div>
            <div id="editBox1" className={styles.editBox}>
                List of current ingredients<br/>Each one can be deleted or edited<br/>Add ingredient form at bottom<br/>How to redorder them??
            </div>
            <div id="editBox2" className={styles.editBox}>
                NOTE - is method currently a list of strings or one big string???<br/>How to reorder items????<br/>delete and edit steps thingo
            </div>
        </div>
    </>
}