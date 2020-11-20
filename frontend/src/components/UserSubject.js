// export type UserObserver = (user_role: string) => void;

class UserSubject {
    constructor(observers, intervalId) {
        this.observers = observers
        this.intervalId = intervalId
    }

    attach(observer) {
        this.observers.push(observer);
    }

    detach(observerToRemove) {
        this.observers = this.observers.filter(observer => observerToRemove != observer)
    }

    updateUser() {
        this.intervalId = setInterval(() => {
            const user = this.fetchUser();
            this.notify(user);
        }, 1000);
    }

    cleanUpdates() {
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
    }

    fetchUser() {
        let user = {
            name: localStorage.getItem('user_name'),
            mail: localStorage.getItem('user_email'),
            roles: [ 'guest' ]
          };
        return user;
    };

    notify(user) {
        this.observers.forEach(observer => observer(user));
    }

}

const userSubject = new UserSubject([], null);

export default userSubject;