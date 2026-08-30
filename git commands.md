.git(local repository tree)\
There is indexing stage(Arrange what to commit) in between working directry and .git These are the 3 tree concept

`.` always refer to the folder we are in\
`..` to directry just above
> In cryptography\
Symmetric/Asymmetric encryption and hashing methods(Can't decrypt unidirrectional function(for things like verification))
## Git basic configurations(History save)
In git file it is pointed towards master(Older) or main(new) and head is pointed to it\
Head is th pointer that shows where to read.
#### git init
To add `.git file` that maintains the versions of the software
#### git add
To add files from working directry to indexing stage \
`.gitignore` contains file what to ignore when git add
#### git commit
To add to git branch from indexing stage.\
Normally first commit is named iitial commit\
When we use `-m <messsage>` it will take commit message without `-m` it pop up text editor then we can write message there\
`git commit -a` add working dir to indexing and commit it to git file `git commit -a -m` or `git commit -am`
> here only changes to files in indexing add changes to indexing and add to git branch \
| Command                                       | What happens                                            | Notes                                                        |
| --------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| `git commit -m "msg"`                         | Commits **only staged files**                           | Does **not** stage modifications or deletions automatically. |
| `git commit -am "msg"`                        | Commits **staged + all modified/deleted tracked files** | Does **not** include new untracked files.                    |
| `git add <new files>` + `git commit -m "msg"` | Commits only the **new files you added**                | Old tracked files stay untouched unless staged for deletion. |


**commit after going backward commit not to main/master bramch it is hard to find those commits unless you commit to _another new branch_**
##### What is the standard message
> first line explanes simply what have done \
empty line - to break line
detail explanation

<a href=https://www.conventionalcommits.org style="color:green;">standards of making commit</a>

#### git status
Can get how nay commits like thing done and `.git` status \
compare indexing stage and work directry

##### git dif `<file>`

shows in detail what has chnged in the file has done.\
`HEAD <file>` compare changes with git branch. 

#### git log

Can see what commits done before head point and what the pointer stage.\
`--oneline` shows only first line of commit

---
#### git checkout
Get the hashcode using `git log` and paste with `git checkout` \
Here head ditach and restore hashcoded version and head points to it
> versions commit after it has hidden
#### git switch
`switch master` use to repoint head to last commit
#### git restore
Use to restore specific file set of a past commit\
`git restore -s <commit char> <file1> <file2> ...`\
`git restore <file1> <file2> ...`
#### git reset
Use to reset whole project to a selected commit.\
`git reset --hard <commit char>`hard reset project to selected commit stage\
here we can't acess commits after reset althoug they exists as main is attached to reset commit.\
If we remember char of them we can acess otherwise we never can.\
After a `git reset --hard`, commits after that are not lost immediately — they can often be recovered via `git reflog` if you know the hash.

----
## [git branches](https://www.youtube.com/watch?v=Uszj_k0DGsg&pp=ygUSZ2l0IGJyYW5jaCBwcm90ZWN00gcJCaIKAYcqIYzv)

#### git branch
To see brances created and where head is
#### creating new branch and deleting branches
`git branch <new branch>` creates new branch from head pointer\
`git branch <new branch> [hash code of branch]` the hash code can get by [git log](#git-log) \
\
`git branch -d <branch name>` deletes <branch name> and cannot delete head branch `-f` can be used to force delete if it warns that it hasn't saved anywhere
#### switching branches
like wise normal head pointer change [`git checkout <branch>`](#git-checkout)\
but better if `git switch <branch>` used
#### Renaming branches
Rename head branch using `git branch -m <branch new name>`\
Another branch by `git branch -m <name of branch> <branch new name>`
#### Tracking branches
`git braanch --track [new branch] <remote branch to track>`\
if new branch is given its head moves to the tracked inside this branch both are same branch here over \
otherwise the branch is get downloaded to loacal repo
#### get git unpulled unpushed status
`git branch -v` ahead -> not pushed behind -> not pulled
#### git merge
need to switch to branch that need to merge into and then what to merge is set through command `git merge <branch that need to merge to another>`
Git Merge Conflict Example

If a file differs in `main` and `feature`, merging shows conflict:
```
line 1
<<<<<< HEAD
Line from main
=======
Line from feature
>>>>>> feature
line 2
```
Resolve by editing, then `git add <file>` and `git commit`.
#### git rebase
No commit at joining its like no branch created and see its a new commit directly
<table>
  <thead>
    <tr>
      <th>Action / Scenario</th>
      <th>Merge</th>
      <th>Rebase</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Checkout branch</td>
      <td><code>git checkout main</code></td>
      <td><code>git checkout feature</code></td>
    </tr>
    <tr>
      <td>Command</td>
      <td><code>git merge feature</code></td>
      <td><code>git rebase main</code></td>
    </tr>
    <tr>
      <td>Resulting history</td>
      <td>
        <pre>
main:    A --- B --- C -------- M
                   \         /
feature:            D --- E
        </pre>
      </td>
      <td>
        <pre>
main:    A --- B --- C
feature:             D' --- E'
        </pre>
      </td>
    </tr>
    <tr>
      <td>Notes</td>
      <td>Merge commit <code>M</code> combines changes from both branches; original commits preserved.</td>
      <td>History is linear; commits <code>D</code> and <code>E</code> are rewritten as <code>D'</code> and <code>E'</code>.</td>
    </tr>
    <tr>
      <td>Merge after Rebase (fast-forward)</td>
      <td>—</td>
      <td>
        <code>git checkout main</code><br>
        <code>git merge feature</code><br>
        <pre>
main/HEAD: A --- B --- C --- D' --- E'
feature:             D' --- E'
        </pre>
        Git does a fast-forward merge; <code>main</code> now includes rebased commits.
      </td>
    </tr>
  </tbody>
</table>

## When comunicate with gitHub, gitLab, BitBuckket

#### git remote
We can manage more than one remote repositories for more cloud bases.
`git remote add <remote name> <cloud url>`\
`git remote remove <remote name>`
#### git push 
To push git branch data to remote to sync with cloud.\
`git push <remote name> <branch>` need to specify at every push\
`git push -u <remote name> <branch>` save remote name and branch so next `git push` is enough\
Here as we need to give credentals again and again we can generate token using github developer setting classical token(ease)
##### git config --global --add credential.helper store
When we log once using username password then it will store it for further use
#### git push for delete branch
`git push <remote> --delete <branch to delete>` `-d` safe delete merged once only `-D` force delete
| Action                                       | Local     | Remote       |
| -------------------------------------------- | --------- | ------------ |
| `git branch -d <branch>`                     | Deleted   | Untouched    |
| `git push origin --delete <branch>`          | Untouched | Deleted      |
| `git branch -d <branch>` + normal `git push` | Deleted   | Still exists |


#### git clone
clone git cloud using `git clone <URL> <Project Name>`

##### git config file
---
in the user file there is a .gitconfig file \
here we can set for two git environments by manually editing file\
`git config --global --list`
> `--local`for project based configurations -> default \
`--system` for OS user based for all user git configuration \
`--global` for our loged user profile

To work with git we have to setup user.name and user.email \
git cofig <`--global`> <`--add`> <`key`> "<`value`>"

###### If you never want to leave Git Bash, you can install GitHub's official command-line tool called gh.

Once gh is installed and you log in (gh auth login), you can manage your entire PR workflow right inside Git Bash:

Push your branch:

```Bash
git push -u origin your-branch-name
```

```bash
# Force push updated history
git push --force-with-lease origin main
```
This push forcely removing our past push data but claim error if last is someone else

Create the Pull Request:

```Bash
gh pr create --title "Your PR Title" --body "Description of your changes"
```
If you omit --title and --body, it will prompt you interactively in Git Bash to type them out.

Check its status later:

```Bash
gh pr status
```

#### Add another repo link in a repo

No, **GitHub does not allow you to link a completely external URL folder natively inside your repository.** However, depending on what you want to achieve, you can use one of these **three standard industry solutions** instead:

---

##### Option 1: Use a Markdown Link (Easiest & Cleanest)

If you just want your readers or examiners to click a button and visit that folder in another GitHub repository, you can simply add a stylized Markdown link anywhere in your `README.md`.

Since we are avoiding splitting your code blocks, here is how you would type it in text:

```text
[📁 View Core Data Pipeline Assets](https://github.com/Username/Repository-Name/tree/main/folder_name)

```

When rendered, it creates a clean folder icon hyperlink that directs the user straight to that precise directory line.

---

##### Option 2: Use GitHub Git Submodules (Advanced Code Linking)

If you need the actual files from that other repository to appear physically inside your local repository workspace like a nested folder, you must use a **Git Submodule**.

To do this, navigate to your root project workspace using PowerShell, and run this standard command:

```powershell
git submodule add https://github.com/Username/Other-Repository-Name.git folder_name_here

```

**How it works:**

* Git creates a tracking link to that exact commit point.
* Inside your GitHub web view, that folder will appear with a special **green folder icon linked with an arrow**, pointing directly to the source repository.
* When people clone your main repository, they can pull down those folder contents automatically.

---

```powershell
git submodule add https://github.com/Username/External-Repository-Name.git external_pipeline
```
enables `[📁 Explore Data Source Folder](./external_pipeline/dataset_processing)` inside README.md file

##### Option 3: Use Git Symlinks (Same Repository Shortcuts)

If the folder already exists inside your current repository and you simply want a shortcut to it at a different directory depth (so you don't copy-paste data and duplicate files), you can create a symlink.

Open your PowerShell terminal as an **Administrator** and execute this Windows command:

```powershell
New-Item -ItemType SymbolicLink -Path "D:\Target_Shortcut_Folder_Path" -Value "D:\Actual_Source_Folder_Path"

```

If you click the file **directly on GitHub's website**, it won't act like a magic hyper-link to the other folder or repository.

Because GitHub's web interface renders a symlink as a plain text file, here is exactly what happens when you click it:

### 📄 What you will see on GitHub

GitHub will just display a single line of text showing the path where the link is pointing.

For example, if you click `link_name.txt`, the page will open and simply display:

```text
..\path\to\target\file.txt

```

### 🛑 Why it doesn't "click through" on the web

GitHub's web browser interface doesn't actively resolve OS-level symbolic links for security and performance reasons. It treats the symlink file as a pointer pointer asset.

### 🎯 The Verdict: Which should you pick?

* If your goal is for **humans to click a link on GitHub's website** to jump to another repo, go back to **Option 1 (The Markdown Link)**.
* If your goal is for **code, scripts, or local developers** to have a working shortcut after they clone the repo down to their machines, stick with **Option 2 (Submodules)** or **Option 3 (Symlinks)**.

Git natively tracks Windows symlinks. When pushed to GitHub, that folder path will function seamlessly as a direct internal routing redirect link!

No, it will **not** clone the submodule files automatically by default when you run a standard `git clone`. Instead, the `external_pipeline` folder will look like an **empty directory** on your computer.

This happens because Git only downloads the small tracking pointer (the specific commit ID) pointing to that external repository, rather than downloading all its files again.

To download the submodule files alongside your main repository, you can use one of these two methods:

### Method 1: Clone everything all at once (Recommended)

If you are cloning the repository for the first time, you can tell Git to fetch the main repository and initialize/download all nested submodules simultaneously by adding the `--recursive` flag:

```powershell
git clone --recursive <your-main-repo-url>

```

### Method 2: Download the files after cloning

If you (or an examiner) have already run a basic `git clone` and noticed that the `external_pipeline` folder is empty, navigate inside your project directory and run this command to pull the submodule files down:

```powershell
git submodule update --init --recursive

```

### 📝 Good Practice for your README

Since this behavior catches many developers off guard, it is highly recommended to add a small note in your `README.md` under the **"How to Run"** section to guide anyone cloning your project:

### 📥 Cloning the Repository (With Submodules)
To ensure all external submodules and pipeline folders are downloaded correctly, clone this repository using the recursive flag:

```powershell
git clone --recursive <your-repository-url>
```

If you have already cloned the repository without the flag, run this command to fetch the missing submodule files:
```powershell
git submodule update --init --recursive
```

If you make changes inside the child folder, commit them, and run `git push` from inside the child folder, **the child repository moves forward in time, but the parent repository is still stuck looking at the old commit hash.**

To fix that mismatch and update the pointer, you have to tell the parent repository to record the child's new version.

---

## The "Two-Commit" Workflow for Updates

Every time you modify code inside your child submodule, you have to follow this exact order to keep both repositories synchronized:

1. **Step 1: Commit & Push inside the Child:** Inside the child folder.
Navigate into your child folder, save your code changes, and push them to the child's independent remote repo:

```bash
cd child-project
git add .
git commit -m "Updated code inside child"
git push origin main

```

*At this exact moment, the child is in the future, and the parent is pointing to the past.*


2. **Step 2: Hop out to the Parent:** Move up one directory.
Move back up into your parent repository's root directory:

```bash
cd ..

```


3. **Step 3: Update the Pointer in the Parent:** Inside the parent folder.
Run `git status`. You will notice that Git flags the child folder as modified because it sees a newer commit available. You need to commit this new position:

```bash
git add child-project
git commit -m "Bump child-project submodule pointer to latest version"
git push origin main

```


---

> 💡 **Pro-Tip from the Video:** To prevent yourself from accidentally pushing a parent repo that points to a version of a child nobody else can access, you can run this command from the parent folder when pushing:
 ```bash
git push --recurse-submodules=check

```

> This acts as a safety net—it will block your parent push if you forgot to push your child changes first!

To create those human-readable version tags (like `v1.0.0`) that `npm` and `pip` can hook onto, you use **Git Tags**.

A Git tag is essentially a permanent bookmark attached to a specific commit hash. Once you push a tag to GitHub, it registers as an official "Release" version.

Here is exactly how to create and push a version tag using Git Bash.

---

## The Workflow to Tag a Version

Navigate into the repository you want to version (for example, your **child repository** folder) and run these commands:

1. **1. Commit your latest changes:** Save code state.
Make sure your working directory is clean and everything is committed:

```bash
git add .
git commit -m "Prepare production release features"

```


2. **2. Create an Annotated Tag:** Local bookmark.
Create a tag using the `-a` flag (stands for annotated). This attaches your name, date, and a version message to the tag—making it a professional release marker:

```bash
git tag -a v1.0.0 -m "Release version 1.0.0 stable"

```


3. **3. Push the Tag to GitHub:** Cloud registry.
Running a standard `git push` **does not** send tags to GitHub. You must explicitly tell Git to push your tags using the `--tags` flag:

```bash
git push origin main --tags

```


---

## 💡 Pro-Tips for Version Tagging

### How to check your existing tags

If you want to see a list of all version tags you have already created in your current project, simply type:

```bash
git tag

```

### Tagging a past commit

If you forgot to tag a version last week and have made 5 new commits since then, you don't have to tag your newest code. You can attach a tag to a past commit by adding its short hash to the end of the command:

```bash
# 1. Find the old commit hash using git log
git log --oneline

# 2. Tag that specific old commit hash (e.g., 4f1a2c3)
git tag -a v0.9.0 -m "Old stable release" 4f1a2c3
git push origin --tags

```

Now that your `v1.0.0` tag is live on GitHub, you can immediately jump into your parent project and pull it using your package manager like a true dependency package:

```bash
npm install git+https://github.com/username/child-repo.git#v1.0.0

```

Good question — this is the **right direction if you want secrets inside a public repo but still keep them protected**.

There are two real-world tools for this: **git-crypt** and **SOPS**. I’ll show you both, but start with the simpler one.

---

# 🔐 Option 1: git-crypt (easier for Git users)

### What it does

* Encrypts selected files inside your repo
* Decrypts automatically for authorized team members
* Others only see encrypted gibberish

---

## ✅ Setup steps

### 1. Install git-crypt

On Windows (Git Bash + Chocolatey):

```bash
choco install git-crypt
```

Or download from:
[https://github.com/AGWA/git-crypt](https://github.com/AGWA/git-crypt)

---

### 2. Initialize in your repo

```bash
git crypt init
```

---

### 3. Tell Git what to encrypt

Create a `.gitattributes` file:

```text
secrets/* filter=git-crypt diff=git-crypt
.env filter=git-crypt diff=git-crypt
```

Example structure:

```text
secrets/api_keys.txt
.env
```

---

### 4. Add your secret file

```bash
echo "API_KEY=12345" > secrets/api_keys.txt
git add secrets/api_keys.txt .gitattributes
git commit -m "Add encrypted secrets"
```

Now it is encrypted in GitHub.

---

### 5. Give access to your team

You must add their GPG key:

```bash
git-crypt add-gpg-user USER_ID
```

Only those users can decrypt.

---

# 🔐 Option 2: Mozilla SOPS (more powerful, modern)

### What it does

* Encrypts JSON, YAML, ENV files
* Uses AWS KMS / GCP / PGP
* Very secure and widely used in DevOps

---

## Example workflow

### Encrypt file:

```bash
sops -e config.json > config.enc.json
```

### Edit securely:

```bash
sops config.json
```

### Commit encrypted file:

```bash
git add config.enc.json
git commit -m "encrypted config"
```

---

# ⚠️ Important truth (very important)

Even with encryption:

* GitHub stores encrypted data publicly
* You are only protecting **content**, not existence
* Anyone can see file names and structure

---

# 🧠 Which one should YOU use?

For your robot / bot project:

### 👉 Use this:

| Need                       | Tool              |
| -------------------------- | ----------------- |
| Simple secret protection   | git-crypt         |
| Professional DevOps system | SOPS              |
| Quick & easy               | .env + .gitignore |

---

# 🚀 Recommended setup for your case

Best practical setup:

```text
.env                (ignored)
config.example.json (public template)
config.json        (local only)
secrets/           (git-crypt encrypted if needed)
```
To mark commit `05d28ad2e17757db69136ec77df9fe924ab2dee6` as **version 1.0.0**, create an annotated tag and push it:

```bash
# Create the tag on the specific commit
git tag -a v1.0.0 05d28ad2e17757db69136ec77df9fe924ab2dee6 -m "Release v1.0.0"

# Create an annotated tag on the latest commit
git tag -a v1.0.0 -m "Release v1.0.0"

# Push the tag to GitHub
git push origin v1.0.0

# Push the tag to GitHub
git push origin v1.0.0
```

To verify:

```bash
git show v1.0.0
```

After pushing, the repository will have a tag named `v1.0.0` pointing permanently to commit `05d28ad2e17757db69136ec77df9fe924ab2dee6`.

If you also want GitHub to show it as a **Release** (with release notes and downloadable source archives), you can create a release from the `v1.0.0` tag in the repository's **Releases** page.
If you renamed **both**:

---

1. The **submodule repository** on GitHub.
2. The **parent repository** on GitHub.

Then each repository must update its own `origin` remote, and the parent must also update the submodule URL.

### In the parent repository

Update the parent's `origin`:

```bash
git remote set-url origin https://github.com/<user>/<new-parent-repo>.git
```

Update the submodule URL in `.gitmodules`:

```bash
git config -f .gitmodules submodule.<submodule-folder>.url https://github.com/<user>/<new-submodule-repo>.git
```

Sync the local configuration:

```bash
git submodule sync --recursive
```

If the submodule already exists locally, also update its own `origin`:

```bash
cd <submodule-folder>
git remote set-url origin https://github.com/<user>/<new-submodule-repo>.git
cd ..
```

Commit the `.gitmodules` change:

```bash
git add .gitmodules
git commit -m "Update submodule URL after repository rename"
git push
```

### If you also renamed the submodule folder

For example:

```text
legacy/  →  fairvision-legacy/
```

that's a separate operation. You'll need to update the `path` in `.gitmodules` and move the submodule correctly. Let me know if you renamed the folder as well, and I can provide the exact commands.

```bash
git log --oneline --decorate --graph --all
```
shows how the working tree of the git


**GitHub Secrets** are encrypted values that GitHub stores securely. They are primarily designed for **GitHub Actions** and are **not** a way to share secret files with people who clone your repository.

### What GitHub Secrets can store

* API keys
* Access tokens
* Passwords
* SSH private keys
* Cloud credentials
* Small text values (not large binary files)

### Example

Suppose your application needs an OpenAI API key.

1. Go to your repository.
2. Open **Settings → Secrets and variables → Actions**.
3. Click **New repository secret**.
4. Create:

```text
Name: OPENAI_API_KEY
Value: sk-xxxxxxxxxxxxxxxx
```

In a GitHub Actions workflow:

```yaml
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

GitHub injects the secret when the workflow runs.

---

## Git subtree: How updates work, parent repo behavior, and how it appears on GitHub

A **git subtree** copies another repository into a folder inside a parent repository while keeping commit history. Unlike a submodule, the child project becomes a **normal folder** in the parent repository.

Example:

```
Samiru-Engineering (parent repo)
│
├── robotics/
│   └── autonomous-robot/       ← subtree from robot repo
│       ├── firmware/
│       ├── hardware/
│       └── README.md
│
├── biomedical/
│   └── medical-ai/             ← subtree from AI repo
│       ├── models/
│       └── train.py
│
└── README.md
```

On GitHub, users see this as a normal folder:

```
📁 robotics
   📁 autonomous-robot
      📄 firmware
      📄 hardware
      📄 README.md

📁 biomedical
   📁 medical-ai
      📄 models
      📄 train.py
```

There is **no submodule link icon**. GitHub treats it like normal files.

---

# 1. Initial subtree import

Parent repository:

```
Samiru-Engineering
```

Child repository:

```
autonomous-robot
```

Add remote:

```bash
git remote add robot https://github.com/user/autonomous-robot.git
```

Fetch:

```bash
git fetch robot
```

Import:

```bash
git subtree add \
--prefix=robotics/autonomous-robot \
robot main
```

Result:

```
Samiru-Engineering
│
└── robotics
    └── autonomous-robot
        ├── firmware
        ├── PCB
        └── README.md
```

A commit is created in the parent:

```
commit abc123
Merge 'robot' as 'robotics/autonomous-robot'
```

---

# 2. Updating parent from child repository

Suppose you modify the original robot repository:

```
autonomous-robot
```

New commit:

```
motor control improved
```

The parent does not automatically know.

You pull changes manually:

```bash
git subtree pull \
--prefix=robotics/autonomous-robot \
robot main
```

Now:

```
Parent repo

before:

robotics/autonomous-robot
     |
     v
old firmware


after:

robotics/autonomous-robot
     |
     v
new firmware
```

A new commit appears:

```
Update subtree robotics/autonomous-robot
```

Then:

```bash
git push origin main
```

---

# 3. Updating child repository from parent

Suppose you edit files inside:

```
robotics/autonomous-robot/
```

inside the parent repo.

Example:

```
robotics/autonomous-robot/firmware/main.cpp
```

Commit:

```bash
git add .
git commit -m "Improve motor controller"
```

Now export changes back:

```bash
git subtree push \
--prefix=robotics/autonomous-robot \
robot main
```

Now the original repository receives the changes.

Flow:

```
              pull
Child Repo  <------  Parent Repo
    ^                  |
    |                  |
    +------ push ------+
```

---

# 4. GitHub commit view

In the parent repository:

```
Commits

✔ Add robot firmware subtree
✔ Update medical AI subtree
✔ Add SLAM documentation
✔ Improve motor controller
```

Clicking:

```
robotics/autonomous-robot
```

shows files normally.

---

# 5. Difference from Git submodule

## Submodule

GitHub view:

```
robotics/
   autonomous-robot @ 4f82a1
```

It shows:

```
autonomous-robot
(submodule)
```

The user must clone recursively:

```bash
git clone --recursive repo
```

---

## Subtree

GitHub view:

```
robotics/
   autonomous-robot/
      firmware/
      PCB/
      README.md
```

No special commands required.

Clone normally:

```bash
git clone https://github.com/user/Samiru-Engineering.git
```

Everything is already there.

---

# 6. Professional monorepo workflow

For a large engineering portfolio:

```
Samiru-Engineering
│
├── robotics
│   ├── autonomous-garden-robot
│   ├── robotic-arm
│   └── SLAM
│
├── biomedical
│   ├── PET-CT-AI
│   ├── MRI-segmentation
│   └── ECG-analysis
│
├── embedded
│   ├── ESP32
│   └── STM32
│
└── simulation
    ├── MATLAB
    └── ANSYS
```

Each project can still have its own repository:

```
github.com/Samiru/autonomous-garden-robot
github.com/Samiru/PET-CT-AI
```

and your portfolio repo:

```
github.com/Samiru/Samiru-Engineering
```

contains them using subtree.

This is a very good structure for a robotics + biomedical engineering portfolio because recruiters can browse one repository while the individual projects still maintain their own histories.


### Can people who clone the repo see GitHub Secrets?

**No.**

* ❌ They are not included in `git clone`.
* ❌ They cannot be viewed in the repository.
* ❌ Even collaborators generally cannot read the stored secret values after they're saved.

Only GitHub Actions workflows (with appropriate permissions) can use them.

---

### Can GitHub Secrets store files?

Not directly.

For example:

* ❌ `certificate.p12`
* ❌ `model.bin`

Instead, you typically:

* Store the file in a private repository or secure storage.
* Or encode a small file as Base64 and save it as a secret, then reconstruct it during a workflow.

---

### Are GitHub Secrets for sharing secrets with authorized developers?

No.

GitHub Secrets are for **automation**, not for distributing secret files to developers. If you want only certain developers to access files, the standard solution is:

* A **private repository**, or
* Secure external storage with access control.

So, if your goal is **"authorized developers can clone and get secret files, while everyone else can clone the public code without the secrets,"** GitHub Secrets are **not** the right tool. A combination of a public repository and a separate private repository (or secure storage) is the recommended approach.
