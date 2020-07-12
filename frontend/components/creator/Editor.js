import styles from "./Edit.module.scss";
import React, { useState } from "react";
import { useRouter } from "next/router";

import RecipeAPI from "../../lib/api/recipe";

import GeneralEdit from "./GeneralEdit";
import MethodEdit from "./MethodEdit";
import IngredientEdit from "./IngredientEdit";

export default function Editor() {
  const [active, setActive] = useState(0);



  function chooseTab(num) {
    document
      .getElementById(`editBox${active}`)
      .classList.remove(styles.showBox);
    setActive(num);
    document.getElementById(`editBox${num}`).classList.add(styles.showBox);
  }
  return (
    <>
      <div id="editor" className={styles.editor}>
        <div className={styles.header}>
          <div className="tabs">
            <ul>
              <li
                onClick={() => chooseTab(0)}
                className={active === 0 ? "is-active" : ""}
              >
                <a>General</a>
              </li>
              <li
                onClick={() => chooseTab(1)}
                className={active === 1 ? "is-active" : ""}
              >
                <a>Ingredients</a>
              </li>
              <li
                onClick={() => chooseTab(2)}
                className={active === 2 ? "is-active" : ""}
              >
                <a>Method</a>
              </li>
            </ul>
          </div>
        </div>

        <div id="editBox0" className={`${styles.editBox} ${styles.showBox}`}>
          <GeneralEdit/>
        </div>
        <div id="editBox1" className={styles.editBox}>
          <IngredientEdit/>
        </div>
        <div id="editBox2" className={styles.editBox}>
          <MethodEdit/>
        </div>

      </div>
    </>
  );
}
