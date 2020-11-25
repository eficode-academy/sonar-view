// export type UserObserver = (user_role: string) => void;

class UserSubject {
    constructor(observers, intervalId) {
        this.observers = observers;
        this.intervalId = intervalId;
    }

    attach(observer) {
        this.observers.push(observer);
    }

    detach(observerToRemove) {
        this.observers = this.observers.filter(observer => observerToRemove !== observer);
    }

    updateUser() {
        this.intervalId = setInterval(() => {
            this.fetchUser();
        }, 1000);
    }

    cleanUpdates() {
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
    }

    fetchUser() {
        const user = {
            name: localStorage.getItem('user_name'),
            mail: localStorage.getItem('user_email'),
            roles: localStorage.getItem('user_role'),
          };
        // console.log(user)
        this.notify(user);
        return user;
    };

    notify(user) {
        this.observers.forEach(observer => observer(user));
    }

}

const userSubject = new UserSubject([], null);

export default userSubject;