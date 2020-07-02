import styles from "./Filer.module.scss";

export default function Filter() {
  return (
    <div>
      <form className={`${styles.filter} form`}>
        <div className="field is-grouped">
          <div className="control">
            <div className="select">
              <select className={styles.option}>
                <option>Breakfast</option>
                <option>Lunch</option>
                <option>Dinner</option>
              </select>
            </div>
          </div>

          <div className="control">
            <div className="select">
              <select className={styles.option}>
                <option>Vegan</option>
                <option>Vegetarian</option>
                <option>Gluten Free</option>
                <option>Dairy Free</option>
              </select>
            </div>
          </div>

          <div className="control">
            <button className={`${styles.option} button is-button`}>
              Update
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}
