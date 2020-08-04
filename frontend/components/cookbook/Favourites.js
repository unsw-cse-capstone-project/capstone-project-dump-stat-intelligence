import styles from "./Cookbook.module.scss";

import { useSelector } from "react-redux";
import RecipeIcon from "./RecipeIcon";
import Arrow from "./Arrow";

export default function Favourites() {
  const favourites = useSelector((state) => state.auth.favourites);
  //Open them to start
  function toggleIt(id) {
    document.getElementById(`${id}-icon`).classList.toggle(styles.arrowUp);
    let box = document.getElementById(`${id}-box`);
    if (box.style.maxHeight) {
      box.style.maxHeight = box.scrollHeight + "px";
      setTimeout(() => {
        box.style.maxHeight = null;
      }, 305);
    } else {
      box.style.maxHeight = box.scrollHeight + "px";
      setTimeout(() => (box.style.maxHeight = "0px"), 5);
    }
  }

  return (
    <>
      <div onClick={() => toggleIt("fave")} className={styles.header}>
        <h1 className="title is-3">Recipes in my cookbook</h1>
        <Arrow name="fave-icon" />
      </div>
      <div id="fave-box" className={`${styles.drawer} columns is-multiline`}>
        <div className={styles.buffer}></div>
        {favourites?.map((recipe, idx) => (
          <div key={idx} className="column is-3">
            <RecipeIcon
              fave={true}
              title={recipe.name}
              id={recipe.id}
              src={recipe.image_URL}
            />
          </div>
        ))}
      </div>
    </>
  );
}
