import styles from "./Cookbook.module.scss";

import { useSelector } from 'react-redux';
import RecipeIcon from "./RecipeIcon";
import Arrow from "./Arrow";

export default function Favourites() {
    const owned = useSelector((state) => state.auth.owned)

    function toggleIt(id) {
        document.getElementById(`${id}-icon`).classList.toggle(styles.arrowUp);
        let box = document.getElementById(`${id}-box`)
        if (box.style.maxHeight) {
          box.style.maxHeight = box.scrollHeight + 'px';
          setTimeout(() => {box.style.maxHeight = null}, 305);
        } else {
          box.style.maxHeight = box.scrollHeight + 'px';
          setTimeout(() => box.style.maxHeight = '0px', 5);
        }
      }


    return <>
        <div onClick={() => toggleIt("owned")} className={styles.header}>
            <h1 className="title is-3">My Owned recipes</h1>
            <Arrow name="owned-icon"/>
        </div> 
        <div id="owned-box" className={`${styles.drawer} columns is-multiline`}>
            <div className={styles.buffer}></div>
            {owned.map((recipe, idx) => (
                <div key={idx} className="column is-3">
                <RecipeIcon fave={true} title={recipe.title} id={recipe.id} src={`https://source.unsplash.com/400x300/?food&sig=${recipe.id}`}/>
                </div>
            ))}
        </div>
    </>
    
}